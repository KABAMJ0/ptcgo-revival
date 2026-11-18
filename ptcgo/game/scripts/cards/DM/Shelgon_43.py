from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
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
    guid="40c412be-a53f-5d70-85b0-c8b26461de78",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shelgon.Name",
    display_name="Shelgon",
    searchable_by=["Shelgon", "Stage 1", "Shelgon"],
    subtypes=["Stage 1"],
    collector_number=43,
    set_code="DM",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bagon.Name",
    family_id=371,
    abilities=[
        Ability(
            title="Energy Guard",
            game_text="If this Pok\u00e9mon has any basic Energy attached to it, it takes 20 less damage from attacks (after applying Weakness and Resistance).",
            passive=takes_less_passive(20, protects=_holder_with(basic_only=True)),
        ),
        Attack(
            title="Rollout",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)