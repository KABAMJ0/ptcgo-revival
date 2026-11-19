from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.card_effects.passives_common import unafflicted
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def _active_volcano(ctx):
    top = ctx.deck_top(1)
    if not top:
        return
    card = top[0]
    await ctx.discard_cards([card])
    if energy_provides_type(card, PokemonTypes.FIRE.value):
        await ctx.attach_energy(card, ctx.attacker)

card = PokemonCardDef(
    guid="8518291e-bf7c-53d0-9342-ca4f2e21e495",
    key="HGSS3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slugma.Name",
    display_name="Slugma",
    searchable_by=["Slugma", "Basic", "Slugma"],
    subtypes=["Basic"],
    collector_number=67,
    set_code="HGSS3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=218,
    abilities=[
        Ability(
            title="Active Volcano",
            game_text="Once during your turn (before your attack), you may discard the top card of your deck. If that card is a Fire Energy card, attach it to Slugma. This power can't be used if Slugma is affected by a Special Condition.",
            activation=Activations.ONCE_PER_TURN,
            condition=unafflicted,
            effect=_active_volcano,
        ),
        Attack(
            title="Combustion",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)
