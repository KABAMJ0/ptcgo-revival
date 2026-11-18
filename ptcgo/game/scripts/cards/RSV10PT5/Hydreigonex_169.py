from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a183b060-9ac1-5f5c-994a-18e89bb6498d",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hydreigonex.Name",
    display_name="Hydreigon ex",
    searchable_by=["Hydreigon ex", "Stage 2", "ex", "Hydreigonex"],
    subtypes=["Stage 2", "ex"],
    collector_number=169,
    set_code="RSV10PT5",
    rarity=Rarities.Rare,
    hp=330,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zweilous.Name",
    family_id=633,
    abilities=[
        Ability(
            title="Greedy Eater",
            game_text="If your opponent's Basic Pok\u00e9mon is Knocked Out by damage from an attack used by this Pok\u00e9mon, take 1 more Prize card.",
            effect=unimplemented,
        ),
        Attack(
            title="Dark Bite",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.DARKNESS: 3, PokemonTypes.COLORLESS: 2},
            damage=200,
            effect=unimplemented,
        ),
    ],
)