from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9af12260-4137-5883-b67d-8b4b34c41724",
    key="HGSS1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Typhlosion.Name",
    display_name="Typhlosion",
    searchable_by=["Typhlosion", "Stage 2", "Prime", "Typhlosion"],
    subtypes=["Stage 2", "Prime"],
    collector_number=110,
    set_code="HGSS1",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Quilava.Name",
    family_id=155,
    abilities=[
        Ability(
            title="Afterburner",
            game_text="Once during your turn (before your attack), you may search your discard pile for a Fire Energy card and attach it to 1 of your Pok\u00e9mon. If you do, put 1 damage counter on that Pok\u00e9mon. This power can't be used if Typhlosion is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Flare Destroy",
            game_text="Discard an Energy card attached to Typhlosion and discard an Energy card attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=unimplemented,
        ),
    ],
)