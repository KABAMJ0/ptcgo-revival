from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="92868d4c-e80b-510b-b216-8699f2fc3f53",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golisopodex.Name",
    display_name="Golisopod ex",
    searchable_by=["Golisopod ex", "Stage 1", "ex", "Golisopodex"],
    subtypes=["Stage 1", "ex"],
    collector_number=50,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=270,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wimpod.Name",
    family_id=767,
    abilities=[
        Attack(
            title="Aqua Blade",
            cost={PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
        Attack(
            title="Swing and Skedaddle",
            game_text="Discard an Energy from this Pok\u00e9mon. If you do, switch it with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=170,
            effect=unimplemented,
        ),
    ],
)