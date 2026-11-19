from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import bonus_if

card = PokemonCardDef(
    guid="46049834-662b-56d5-bc1f-fed3023c9c69",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronLeaves.Name",
    display_name="Iron Leaves",
    searchable_by=["Iron Leaves", "Basic", "Future", "IronLeaves"],
    subtypes=["Basic", "Future"],
    collector_number=19,
    set_code="SV6",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=1010,
    abilities=[
        Attack(
            title="Recovery Net",
            game_text="Put up to 2 Pok\u00e9mon from your discard pile into your hand.",
            cost={PokemonTypes.GRASS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Avenging Edge",
            game_text="If any of your Pok\u00e9mon were Knocked Out by damage from an attack during your opponent's last turn, this attack does 60 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="+",
            effect=bonus_if(lambda ctx: ctx.kos_suffered_last_turn(ctx.player_id) > 0, 60),
        ),
    ],
)