from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import snipe_attack

card = PokemonCardDef(
    guid="5273becc-b146-5c48-ab2f-e50862b5414a",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HonchkrowG.Name",
    display_name="Honchkrow G",
    searchable_by=["Honchkrow G", "Basic", "SP", "HonchkrowG"],
    subtypes=["Basic", "SP"],
    collector_number=77,
    set_code="PL1",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=430,
    abilities=[
        Attack(
            title="Honcho's Command",
            game_text="Search your deck for up to 2 in any combination of Stadium cards or Trainer cards that has Team Galactic's Invention in its name, show them to your opponent, and put them into your hand. Shuffle your deck afterward.",
            cost={},
            effect=unimplemented,
        ),
        Attack(
            title="Target Attack",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 20 damage to that Pok\u00e9mon. If that Pok\u00e9mon already has any damage counters on it, this attack does 20 damage plus 20 more damage. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            effect=snipe_attack(20, pool="any", count=1, apply_modifiers=False),
        ),
    ],
)