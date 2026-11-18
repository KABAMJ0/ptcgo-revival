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
    guid="50280326-6540-5fd4-9c09-e71bd2617609",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lunala.Name",
    display_name="Lunala",
    searchable_by=["Lunala", "Stage 2", "Lunala"],
    subtypes=["Stage 2"],
    collector_number=70,
    set_code="SM7",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cosmoem.Name",
    family_id=792,
    abilities=[
        Ability(
            title="Shadow Shield",
            game_text="If this Pok\u00e9mon has any Psychic Energy attached to it, it takes 20 less damage from attacks (after applying Weakness and Resistance).",
            passive=takes_less_passive(20, protects=_holder_with(PokemonTypes.PSYCHIC.value)),
        ),
        Attack(
            title="Full Moon Ray",
            game_text="This attack does 20 more damage times the amount of Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=80,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)