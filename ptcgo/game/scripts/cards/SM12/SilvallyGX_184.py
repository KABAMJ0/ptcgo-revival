from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import draw_until_effect
from ptcgo.game.card_effects.attacks_common import bonus_if


def _supporter_played_this_turn(ctx):
    return ctx.supporters_played_this_turn() > 0


card = PokemonCardDef(
    guid="d54cefe1-f675-5d79-99b8-a6865eb8834d",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SilvallyGX.Name",
    display_name="Silvally-GX",
    searchable_by=["Silvally-GX", "Stage 1", "GX", "SilvallyGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=184,
    set_code="SM12",
    rarity=Rarities.RareHolo,
    hp=210,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TypeNull.Name",
    family_id=772,
    abilities=[
        Ability(
            title="Disk Reload",
            game_text="Once during your turn (before your attack), you may draw cards until you have 5 cards in your hand.",
            activation=Activations.ONCE_PER_TURN,
            effect=draw_until_effect(5),
        ),
        Attack(
            title="Brave Buddies",
            game_text="If you played a Supporter card from your hand during this turn, this attack does 70 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=bonus_if(_supporter_played_this_turn, 70),
        ),
        Attack(
            title="Silver Knight-GX",
            game_text="If your opponent's Active Pok\u00e9mon is an Ultra Beast, it is Knocked Out. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
    ],
)