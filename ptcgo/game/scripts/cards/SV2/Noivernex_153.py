from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4015f090-2918-57da-b926-bb8ac956ec99",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Noivernex.Name",
    display_name="Noivern ex",
    searchable_by=["Noivern ex", "Stage 1", "ex", "Noivernex"],
    subtypes=["Stage 1", "ex"],
    collector_number=153,
    set_code="SV2",
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