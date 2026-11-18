from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, subtypes_for, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import snipe_attack
from ptcgo.game.card_effects.passives_common import is_in_active_spot


def _is_benched_gx_or_ex(pokemon) -> bool:
    subtypes = subtypes_for(pokemon.archetype_id)
    return ("GX" in subtypes or "EX" in subtypes) and not is_in_active_spot(pokemon)

card = PokemonCardDef(
    guid="f0cf1d7a-3447-5f4e-a03f-5b16a51f091b",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UmbreonDarkraiGX.Name",
    display_name="Umbreon & Darkrai-GX",
    searchable_by=["Umbreon & Darkrai-GX", "Basic", "TAG TEAM", "GX", "UmbreonDarkraiGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=241,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=270,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=197,
    abilities=[
        Attack(
            title="Black Lance",
            game_text="This attack does 60 damage to 1 of your opponent's Benched Pok\u00e9mon-GX or Benched Pok\u00e9mon-EX. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=snipe_attack(60, pool=_is_benched_gx_or_ex, count=1),
        ),
        Attack(
            title="Dark Moon-GX",
            game_text="Your opponent can't play any Trainer cards from their hand during their next turn. If this Pok\u00e9mon has at least 5 extra Darkness Energy attached to it (in addition to this attack's cost), your opponent's Active Pok\u00e9mon is Knocked Out. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)