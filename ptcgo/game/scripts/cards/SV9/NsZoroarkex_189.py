from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="599ccd0b-3b0b-51e7-8c01-af2bd54c2cf6",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NsZoroarkex.Name",
    display_name="N's Zoroark ex",
    searchable_by=["N's Zoroark ex", "Stage 1", "ex", "NsZoroarkex"],
    subtypes=["Stage 1", "ex"],
    collector_number=189,
    set_code="SV9",
    rarity=Rarities.Rare,
    hp=280,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.NsZorua.Name",
    family_id=570,
    abilities=[
        Ability(
            title="Trade",
            game_text="You must discard a card from your hand in order to use this Ability. Once during your turn, you may draw 2 cards.",
            effect=unimplemented,
        ),
        Attack(
            title="Night Joker",
            game_text="Choose 1 of your Benched N's Pok\u00e9mon's attacks and use it as this attack.",
            cost={PokemonTypes.DARKNESS: 2},
            effect=unimplemented,
        ),
    ],
)