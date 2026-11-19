from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Triggers
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities, SpecialConditions


async def _harvest_bounty(ctx):
    if ctx.source is not None and ctx.source.get_attribute(AttrID.SPECIAL_CONDITIONS):
        return
    active = ctx.my_active()
    if active is None or ctx.energy_receiver is not active:
        return
    if ctx.attaching_player_id != ctx.player_id:
        return
    ctx.allow_extra_attachment(1)

card = PokemonCardDef(
    guid="4788a690-b838-529f-92ee-55aae2f95dc8",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Venusaur.Name",
    display_name="Venusaur",
    searchable_by=["Venusaur", "Stage 2", "Venusaur"],
    subtypes=["Stage 2"],
    collector_number=30,
    set_code="ECARD1",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ivysaur.Name",
    family_id=1,
    abilities=[
        Ability(
            title="Harvest Bounty",
            game_text="Once during your turn (before your attack), if you attach an Energy card to your Active Pok\u00e9mon as part of your turn, you may attach an additional Energy card to that Pok\u00e9mon at the same time. This power can't be used if Venusaur is affected by a Special Condition.",
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=_harvest_bounty,
        ),
        Attack(
            title="Body Slam",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)