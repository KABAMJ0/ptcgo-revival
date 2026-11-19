from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="01ea1a10-0067-5327-a94a-a859f8ce85f2",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ninetales.Name",
    display_name="Ninetales",
    searchable_by=["Ninetales", "Stage 1", "Ninetales"],
    subtypes=["Stage 1"],
    collector_number=27,
    set_code="SV6",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name",
    family_id=37,
    abilities=[
        Attack(
            title="Eerie Glow",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned and Confused.",
            cost={PokemonTypes.FIRE: 2},
            damage=90,
            effect=condition_attack(SpecialConditions.BURNED, SpecialConditions.CONFUSED),
        ),
    ],
)