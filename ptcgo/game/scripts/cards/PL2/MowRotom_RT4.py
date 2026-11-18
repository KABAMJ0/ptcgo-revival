from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="717d9223-723b-502a-a974-e09bc41a34f3",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MowRotom.Name",
    display_name="Mow Rotom",
    searchable_by=["Mow Rotom", "Basic", "MowRotom"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="PL2",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.COLORLESS,
    family_id=479,
    abilities=[
        Ability(
            title="Mow Shift",
            game_text="Once during your turn (before your attack), you may use this power. Mow Rotom's type is Grass until the end of your turn.",
            effect=unimplemented,
        ),
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Mow Down",
            game_text="Flip a coin. If heads, discard an Energy card attached to each of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=unimplemented,
        ),
    ],
)