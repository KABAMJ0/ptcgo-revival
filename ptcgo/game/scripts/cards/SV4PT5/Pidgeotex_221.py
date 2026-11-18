from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="16a4c6b0-2658-519e-b3d5-e18c26c6451b",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgeotex.Name",
    display_name="Pidgeot ex",
    searchable_by=["Pidgeot ex", "Stage 2", "ex", "Pidgeotex"],
    subtypes=["Stage 2", "ex"],
    collector_number=221,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=280,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgeotto.Name",
    family_id=16,
    abilities=[
        Ability(
            title="Quick Search",
            game_text="Once during your turn, you may search your deck for a card and put it into your hand. Then, shuffle your deck. You can't use more than 1 Quick Search Ability each turn.",
            effect=unimplemented,
        ),
        Attack(
            title="Blustery Wind",
            game_text="You may discard a Stadium in play.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=unimplemented,
        ),
    ],
)