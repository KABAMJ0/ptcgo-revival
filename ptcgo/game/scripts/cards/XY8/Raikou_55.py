from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import takes_less_passive
from ptcgo.game.card_effects.pokemon import energy_provides_type, is_energy_card
from ptcgo.game.session.effects import is_special_energy
from ptcgo.game.session.passives import carrier_pokemon
from ptcgo.game.card_effects.attacks_common import count_energy
from ptcgo.game.card_effects.attacks_common import damage_per
from ptcgo.game.card_effects.attacks_common import count_energy, damage_per


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
    guid="a630362e-3388-54d6-8cb7-0b671f8ad161",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raikou.Name",
    display_name="Raikou",
    searchable_by=["Raikou", "Basic", "Raikou"],
    subtypes=["Basic"],
    collector_number=55,
    set_code="XY8",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=243,
    abilities=[
        Ability(
            title="Shining Body",
            game_text="If this Pok\u00e9mon has any Lightning Energy attached to it, any damage done to this Pok\u00e9mon by attacks is reduced by 20 (after applying Weakness and Resistance).",
            passive=takes_less_passive(20, protects=_holder_with(PokemonTypes.LIGHTNING.value)),
        ),
        Attack(
            title="Thunder Lance",
            game_text="This attack does 20 more damage for each Lightning Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator="+",
            effect=damage_per(count_energy("self", PokemonTypes.LIGHTNING), per=20, base=50),
        ),
    ],
)