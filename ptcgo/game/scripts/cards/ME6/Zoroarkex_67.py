from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8b625dfe-40af-5f03-8352-5947908b4c2f",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zoroarkex.Name",
    display_name="Zoroark ex",
    searchable_by=["Zoroark ex", "Stage 1", "ex", "Zoroarkex"],
    subtypes=["Stage 1", "ex"],
    collector_number=67,
    set_code="ME6",
    rarity=Rarities.Rare,
    hp=270,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zorua.Name",
    family_id=570,
    abilities=[
        Attack(
            title="Riotous Beating",
            game_text="This attack does 20 damage for each of your Pok\u00e9mon in play.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Slashing Strike",
            game_text="During your next turn, this Pok\u00e9mon can't use Slashing Strike.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=210,
            effect=unimplemented,
        ),
    ],
)