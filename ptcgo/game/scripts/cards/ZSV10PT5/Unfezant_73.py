from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import draw_attack
from ptcgo.game.card_effects.passives_common import flip_protection


card = PokemonCardDef(
    guid="d22f0bbf-b50c-548f-9bb5-dfbf60572b59",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Unfezant.Name",
    display_name="Unfezant",
    searchable_by=["Unfezant", "Stage 2", "Unfezant"],
    subtypes=["Stage 2"],
    collector_number=73,
    set_code="ZSV10PT5",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tranquill.Name",
    family_id=519,
    abilities=[
        Attack(
            title="Add On",
            game_text="Draw 4 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=draw_attack(4),
        ),
        Attack(
            title="Swift Flight",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=flip_protection(prevent=True, effects_too=True),
        ),
    ],
)