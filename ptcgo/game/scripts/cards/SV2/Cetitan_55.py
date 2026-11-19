from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.effects import is_special_energy
from ptcgo.game.card_effects.attacks_common import bonus_if

card = PokemonCardDef(
    guid="5ddd1841-9903-5bf7-8c2e-a7e51a1ee59d",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cetitan.Name",
    display_name="Cetitan",
    searchable_by=["Cetitan", "Stage 1", "Cetitan"],
    subtypes=["Stage 1"],
    collector_number=55,
    set_code="SV2",
    rarity=Rarities.Uncommon,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cetoddle.Name",
    family_id=974,
    abilities=[
        Attack(
            title="Icicle Missile",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title="Special Horn",
            game_text="If this Pok\u00e9mon has any Special Energy attached, this attack does 140 more damage.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=bonus_if(lambda ctx: any(is_special_energy(e) for e in ctx.attached_energies(ctx.attacker)), 140),
        ),
    ],
)