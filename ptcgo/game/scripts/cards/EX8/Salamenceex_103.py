from ptcgo.game.card_effects.attacks_common import snipe_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a2a345fb-4776-5a14-8e9c-1f40f22bad98",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Salamenceex.Name",
    display_name="Salamence ex",
    searchable_by=["Salamence ex", "Stage 2", "ex", "Salamenceex"],
    subtypes=["Stage 2", "ex"],
    collector_number=103,
    set_code="EX8",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shelgon.Name",
    family_id=371,
    abilities=[
        Ability(
            title="Dragon Lift",
            game_text="The Retreat Cost for each of your Pok\u00e9mon (excluding Pok\u00e9mon-ex and Baby Pok\u00e9mon) is 0.",
            effect=unimplemented,
        ),
        Attack(
            title="Flame Jet",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 40 damage to that Pok\u00e9mon. This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            effect=snipe_attack(40, pool="any", apply_modifiers=False),
        ),
        Attack(
            title="Bright Flame",
            game_text="Discard 2 Energy attached to Salamence ex.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=unimplemented,
        ),
    ],
)