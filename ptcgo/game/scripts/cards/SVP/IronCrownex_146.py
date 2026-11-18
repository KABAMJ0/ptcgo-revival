from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import snipe_attack

card = PokemonCardDef(
    guid="549a47ef-4872-5b55-8b59-9b32da4537fe",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronCrownex.Name",
    display_name="Iron Crown ex",
    searchable_by=["Iron Crown ex", "Basic", "ex", "Future", "IronCrownex"],
    subtypes=["Basic", "ex", "Future"],
    collector_number=146,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=220,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    abilities=[
        Ability(
            title="Cobalt Command",
            game_text="Attacks used by your Future Pok\u00e9mon, except any Iron Crown ex, do 20 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Twin Shotels",
            game_text="This attack does 50 damage to 2 of your opponent's Pok\u00e9mon. This attack's damage isn't affected by Weakness or Resistance, or by any effects on those Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            effect=snipe_attack(50, pool="any", count=2, apply_modifiers=False),
        ),
    ],
)