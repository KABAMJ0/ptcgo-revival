from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e61f7747-73b4-5463-b650-a0f8525b55f0",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dialga.Name",
    display_name="Dialga",
    searchable_by=["Dialga", "Basic", "Dialga"],
    subtypes=["Basic"],
    collector_number=23,
    set_code="PL1",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=483,
    abilities=[
        Attack(
            title="Energy Stream",
            game_text="Flip a coin. If heads, search your discard pile for a basic Energy card and attach it to Dialga.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Diamond Blow",
            game_text="Dialga can't attack during your next turn.",
            cost={PokemonTypes.METAL: 3, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=unimplemented,
        ),
    ],
)