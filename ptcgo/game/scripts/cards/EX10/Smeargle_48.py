from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fb158a75-1828-5f42-9006-63be10a64d9c",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Smeargle.Name",
    display_name="Smeargle",
    searchable_by=["Smeargle", "Basic", "Smeargle"],
    subtypes=["Basic"],
    collector_number=48,
    set_code="EX10",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=235,
    abilities=[
        Ability(
            title="Makeover",
            game_text="Once during your turn (before your attack), you may discard a basic Energy card attached to 1 of your Pok\u00e9mon (excluding Pok\u00e9mon-ex). If you do, search your discard pile for a basic Energy card (excluding the one you discarded) and attach it to that Pok\u00e9mon. This power can't be used if Smeargle is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Split Spiral Punch",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=unimplemented,
        ),
    ],
)