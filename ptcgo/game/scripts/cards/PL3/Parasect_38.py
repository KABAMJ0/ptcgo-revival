from ptcgo.game.card_effects.support_common import search_attach_energy
from ptcgo.game.card_effects.trainers import basic_energy_of
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="546808b7-d70c-591b-bf16-c6857264531b",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Parasect.Name",
    display_name="Parasect",
    searchable_by=["Parasect", "Stage 1", "Parasect"],
    subtypes=["Stage 1"],
    collector_number=38,
    set_code="PL3",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Paras.Name",
    family_id=46,
    abilities=[
        Attack(
            title="Nutritional Support",
            game_text="Search your deck for up to 2 Grass Energy cards and attach them to any of your Pok\u00e9mon in any way you like. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_attach_energy(basic_energy_of("Grass"), count=2, distribute=True),
        ),
        Attack(
            title="Hibernation Spore",
            game_text="The Defending Pok\u00e9mon is now Asleep. Flip 2 coins instead of 1 between turns. If either of them is tails, the Defending Pok\u00e9mon is still Asleep.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=unimplemented,
        ),
    ],
)