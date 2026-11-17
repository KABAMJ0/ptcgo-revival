from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="668e3103-8d87-5eff-ad93-cb905ce253ac",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aerodactyl.Name",
    display_name="Aerodactyl",
    searchable_by=["Aerodactyl", "Stage 1", "Aerodactyl"],
    subtypes=["Stage 1"],
    collector_number=13,
    set_code="PL4",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.OldAmber.Name",
    family_id=142,
    abilities=[
        Ability(
            title="Unearth",
            game_text="Once during your turn (before your attack), you may search your deck for Helix Fossil, Dome Fossil, or Old Amber, show it your opponent, and put it into your hand. Shuffle your deck afterward. This power can't be used if Aerodactyl is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Hyper Beam",
            game_text="Flip a coin. If heads, discard an Energy card attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=unimplemented,
        ),
    ],
)