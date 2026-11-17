from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1b1cfc48-9be9-56b4-8da5-3eda3878911c",
    key="SMA",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GardevoirGX.Name",
    display_name="Gardevoir-GX",
    searchable_by=["Gardevoir-GX", "Stage 2", "GX", "GardevoirGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=75,
    set_code="SMA",
    rarity=Rarities.Rare,
    hp=230,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name",
    family_id=280,
    abilities=[
        Ability(
            title="Secret Spring",
            game_text="Once during your turn (before your attack), you may attach a Fairy Energy card from your hand to 1 of your Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Infinite Force",
            game_text="This attack does 30 damage times the amount of Energy attached to both Active Pok\u00e9mon.",
            cost={PokemonTypes.FAIRY: 1},
            damage=30,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Twilight-GX",
            game_text="Shuffle 10 cards from your discard pile into your deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FAIRY: 1},
            effect=unimplemented,
        ),
    ],
)