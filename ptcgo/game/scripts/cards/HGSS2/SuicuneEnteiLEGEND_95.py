from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="66b370a0-b871-555b-a365-ab24ca05230c",
    key="HGSS2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SuicuneEnteiLEGEND.Name",
    display_name="Suicune & Entei LEGEND",
    searchable_by=["Suicune & Entei LEGEND", "LEGEND", "SuicuneEnteiLEGEND"],
    subtypes=["LEGEND"],
    collector_number=95,
    set_code="HGSS2",
    rarity=Rarities.Common,
    hp=160,
    elements=[PokemonTypes.WATER, PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=244,
    abilities=[
        Attack(
            title="Torrent Blade",
            game_text="Return 2 Water Energy attached to Suicune & Entei LEGEND to your hand. Choose 1 of your opponent's Benched Pok\u00e9mon. This attack does 100 damage to that Pok\u00e9mon. (Don't apply Weakness or Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Bursting Inferno",
            game_text="The Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=condition_attack(SpecialConditions.BURNED),
        ),
    ],
)