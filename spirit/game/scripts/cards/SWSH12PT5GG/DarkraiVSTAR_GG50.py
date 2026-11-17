from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="12bd9548-97f3-5839-9e36-395b072d7785",
    key="SWSH12PT5GG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkraiVSTAR.Name",
    display_name="Darkrai VSTAR",
    searchable_by=["Darkrai VSTAR", "VSTAR", "DarkraiVSTAR"],
    subtypes=["VSTAR"],
    collector_number=50,
    set_code="SWSH12PT5GG",
    rarity=Rarities.RareHoloVSTAR,
    hp=270,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DarkraiV.Name",
    family_id=491,
    abilities=[
        Ability(
            title="Star Abyss",
            game_text="During your turn, you may put up to 2 Item cards from your discard pile into your hand. (You can't use more than 1 VSTAR Power in a game.)",
            effect=unimplemented,
        ),
        Attack(
            title="Dark Pulse",
            game_text="This attack does 30 more damage for each Darkness Energy attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)