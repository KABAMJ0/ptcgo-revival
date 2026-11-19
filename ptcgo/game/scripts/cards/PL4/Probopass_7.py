from ptcgo.game.card_effects.support_common import draw_attack
from ptcgo.game.card_effects.attacks_common import flip_damage, flip_gate
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import draw_attack

card = PokemonCardDef(
    guid="ed7ec7cf-c306-5376-9740-924a9d2e19b5",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Probopass.Name",
    display_name="Probopass",
    searchable_by=["Probopass", "Stage 1", "Probopass"],
    subtypes=["Stage 1"],
    collector_number=7,
    set_code="PL4",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nosepass.Name",
    family_id=299,
    abilities=[
        Ability(
            title="Competitiveness",
            game_text="If you don't have a Supporter card in play, each of Probopass's attacks does 30 more damage to the Active Pok\u00e9mon (before applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Top Chop",
            game_text="Draw a card.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=draw_attack(1),
        ),
        Attack(
            title="Tumbling Attack",
            game_text="Flip a coin. If heads, this attack does 50 damage plus 30 more damage.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=flip_gate(then=lambda ctx: ctx.deal_damage(80)),
        ),
    ],
)