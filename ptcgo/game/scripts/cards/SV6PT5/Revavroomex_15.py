from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import bonus_if, snipe_attack
card = PokemonCardDef(
    guid="b62c3393-f99c-535c-9cff-3b15d8a1e429",
    key="SV6PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Revavroomex.Name",
    display_name="Revavroom ex",
    searchable_by=["Revavroom ex", "Stage 1", "Tera", "ex", "Revavroomex"],
    subtypes=["Stage 1", "Tera", "ex"],
    collector_number=15,
    set_code="SV6PT5",
    rarity=Rarities.Rare,
    hp=280,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Varoom.Name",
    family_id=965,
    abilities=[
        Attack(
            title="Accelerator Flash",
            game_text="If this Pok\u00e9mon moved from your Bench to the Active Spot this turn, this attack does 120 more damage.",
            cost={PokemonTypes.METAL: 1},
            damage=20,
            damage_operator="+",
            effect=bonus_if(lambda ctx: ctx.entered_active_this_turn(ctx.attacker), 120),
        ),
        Attack(
            title="Shattering Speed",
            game_text="Discard this Pok\u00e9mon and all attached cards.",
            cost={PokemonTypes.METAL: 3},
            damage=250,
            effect=unimplemented,
        ),
    ],
)