from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="59d5c41d-0639-5fc4-acde-8806d99276f2",
    key="DPP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DialgaLVX.Name",
    display_name="Dialga LV.X",
    searchable_by=["Dialga LV.X", "Level-Up", "DialgaLVX"],
    subtypes=["Level-Up"],
    collector_number=17,
    set_code="DPP",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dialga.Name",
    family_id=483,
    abilities=[
        Ability(
            title="Time Skip",
            game_text="Once during your turn (before your attack), you may have your opponent flip 2 coins. If both of them are heads, your turn ends. If both of them are tails, after your opponent draws a card at the beginning of his or her next turn, his or her turn ends. This power can't be used if Dialga is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Metal Flash",
            game_text="During your next turn, Dialga can't use Metal Flash.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=unimplemented,
        ),
    ],
)