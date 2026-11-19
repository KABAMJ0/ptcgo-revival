from ptcgo.game.card_effects.attacks_common import reveal_hand_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


card = PokemonCardDef(
    guid="0f36dd67-7c1d-5aa2-96e1-16db5548fd03",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sigilyph.Name",
    display_name="Sigilyph",
    searchable_by=["Sigilyph", "Basic", "Sigilyph"],
    subtypes=["Basic"],
    collector_number=55,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=561,
    abilities=[
        Attack(
            title="Reflective Shield",
            game_text="During your opponent's next turn, if this Pok\u00e9mon is damaged by an attack (even if this Pok\u00e9mon is Knocked Out), put 5 damage counters on the Attacking Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=reveal_hand_attack(),
        ),
        Attack(
            title="Psy Report",
            game_text="Your opponent reveals his or her hand.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=30,
            effect=reveal_hand_attack(),
        ),
    ],
)