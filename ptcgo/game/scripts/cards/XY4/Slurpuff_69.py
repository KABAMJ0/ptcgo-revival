from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f24b1e63-468d-5859-bf82-75d23d44965d",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slurpuff.Name",
    display_name="Slurpuff",
    searchable_by=["Slurpuff", "Stage 1", "Slurpuff"],
    subtypes=["Stage 1"],
    collector_number=69,
    set_code="XY4",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Swirlix.Name",
    family_id=684,
    abilities=[
        Ability(
            title="Tasting",
            game_text="Once during your turn (before your attack), you may draw a card. If this Pok\u00e9mon is your Active Pok\u00e9mon, draw 1 more card.",
            effect=unimplemented,
        ),
        Attack(
            title="Light Pulse",
            game_text="Prevent all effects of your opponent's attacks, except damage, done to this Pok\u00e9mon during your opponent's next turn.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=unimplemented,
        ),
    ],
)