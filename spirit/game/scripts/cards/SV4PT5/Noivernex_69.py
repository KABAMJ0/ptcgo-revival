from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="04a9159e-5df1-53e4-bdd5-88ac3e860032",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Noivernex.Name",
    display_name="Noivern ex",
    searchable_by=["Noivern ex", "Stage 1", "ex", "Noivernex"],
    subtypes=["Stage 1", "ex"],
    collector_number=69,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=260,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Noibat.Name",
    family_id=714,
    abilities=[
        Attack(
            title="Covert Flight",
            game_text="During your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks from Basic Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=unimplemented,
        ),
        Attack(
            title="Dominating Echo",
            game_text="During your opponent's next turn, they can't play any Special Energy or Stadium cards from their hand.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.DARKNESS: 1},
            damage=140,
            effect=unimplemented,
        ),
    ],
)