from ptcgo.game.data_utils import Ability, Attack, PokemonCardDef, unimplemented
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities
from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import takes_less_passive
from ptcgo.game.card_effects.pokemon import energy_provides_type, is_energy_card
from ptcgo.game.session.effects import is_special_energy
from ptcgo.game.session.passives import carrier_pokemon


def _holder_with(type_value=None, basic_only=False):
    def protects(target, carrier):
        if carrier_pokemon(carrier) is not target:
            return False
        for child in target.children or []:
            if not is_energy_card(child):
                continue
            if basic_only and is_special_energy(child):
                continue
            if type_value is None or energy_provides_type(child, type_value):
                return True
        return False
    return protects

card = PokemonCardDef(
    guid="a05c9df1-5124-5673-bc2a-52e4ef200468",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HippowdonE4.Name",
    display_name="Hippowdon E4",
    searchable_by=["Hippowdon E4", "Basic", "SP", "HippowdonE4"],
    subtypes=["Basic", "SP"],
    collector_number=42,
    set_code="PL2",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    family_id=450,
    abilities=[
        Ability(
            title="Sand Armor",
            game_text="If Hippowdon E4 has any Fighting Energy attached to it, any damage done to Hippowdon E4 by attacks is reduced by 10 (after applying Weakness and Resistance).",
            passive=takes_less_passive(10, protects=_holder_with(PokemonTypes.FIGHTING.value)),
        ),
        Attack(
            title="Bite and Crush",
            game_text="Flip 2 coins. This attack does 30 damage plus 10 more damage for each heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="+",
            effect=flip_damage(coins=2, base=30, bonus_per_heads=10),
        ),
    ],
)