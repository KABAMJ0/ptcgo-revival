from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2865225b-0ed4-5cda-a726-f925ffa060f5",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Typhlosion.Name",
    display_name="Typhlosion δ",
    searchable_by=["Typhlosion \u03b4", "Stage 2", "Typhlosion"],
    subtypes=["Stage 2"],
    collector_number=12,
    set_code="EX15",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Quilava.Name",
    family_id=157,
    abilities=[
        Ability(
            title="Shady Move",
            game_text="Once during your turn (before your attack), if Typhlosion is your Active Pok\u00e9mon, you may move 1 damage counter from either player's Pok\u00e9mon to another Pok\u00e9mon (yours or your opponent's). This power can't be used if Typhlosion is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Burning Ball",
            game_text="If Typhlosion has at least 2 Fire Energy attached to it, the Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=unimplemented,
        ),
    ],
)