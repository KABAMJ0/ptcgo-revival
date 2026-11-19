from ptcgo.game.card_effects.support_common import remove_self_from_play
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="62196e0f-d111-543b-b346-73abeb73bb03",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsCrobatex.Name",
    display_name="Team Rocket's Crobat ex",
    searchable_by=["Team Rocket's Crobat ex", "Stage 2", "ex", "TeamRocketsCrobatex"],
    subtypes=["Stage 2", "ex"],
    collector_number=122,
    set_code="SV10",
    rarity=Rarities.Rare,
    hp=310,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsGolbat.Name",
    family_id=41,
    abilities=[
        Ability(
            title="Biting Spree",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may choose 2 of your opponent's Pok\u00e9mon and put 2 damage counters on each of them.",
            effect=unimplemented,
        ),
        Attack(
            title="Assassin's Return",
            game_text="You may put this Pok\u00e9mon into your hand. (Discard all cards attached to this Pok\u00e9mon.)",
            cost={PokemonTypes.DARKNESS: 2},
            damage=120,
            effect=remove_self_from_play("hand", with_attachments="discard", optional=True),
        ),
    ],
)