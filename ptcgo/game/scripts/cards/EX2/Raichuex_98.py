from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a943cbc0-75dc-54c2-96dd-43c336a5efbf",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raichuex.Name",
    display_name="Raichu ex",
    searchable_by=["Raichu ex", "Stage 1", "ex", "Raichuex"],
    subtypes=["Stage 1", "ex"],
    collector_number=98,
    set_code="EX2",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    family_id=25,
    abilities=[
        Attack(
            title="Dazzle Blast",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Mega Thunderbolt",
            game_text="Discard all Energy cards attached to Raichu ex.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=unimplemented,
        ),
    ],
)