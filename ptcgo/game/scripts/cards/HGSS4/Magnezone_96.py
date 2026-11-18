from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1f7c3624-13ff-5839-a116-11d0b13c28af",
    key="HGSS4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magnezone.Name",
    display_name="Magnezone",
    searchable_by=["Magnezone", "Stage 2", "Prime", "Magnezone"],
    subtypes=["Stage 2", "Prime"],
    collector_number=96,
    set_code="HGSS4",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magneton.Name",
    family_id=81,
    abilities=[
        Ability(
            title="Magnetic Draw",
            game_text="Once during your turn (before your attack), you may draw cards until you have 6 cards in your hand. This power can't be used if Magnezone is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Lost Burn",
            game_text="Put as many Energy cards attached to your Pok\u00e9mon as you like in the Lost Zone. This attack does 50 damage times the number of Energy cards put in the Lost Zone in this way.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)