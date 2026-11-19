from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.effects import is_special_energy
from ptcgo.game.card_effects.attacks_common import bonus_if

card = PokemonCardDef(
    guid="39d04351-7551-5b1c-bcf4-39c47986762b",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stoutland.Name",
    display_name="Stoutland",
    searchable_by=["Stoutland", "Stage 2", "Stoutland"],
    subtypes=["Stage 2"],
    collector_number=76,
    set_code="RSV10PT5",
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Herdier.Name",
    family_id=506,
    abilities=[
        Attack(
            title="Odor Sleuth",
            game_text="Flip 3 coins. Put a number of cards up to the number of heads from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Special Fang",
            game_text="If this Pok\u00e9mon has any Special Energy attached, this attack does 100 more damage.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=100,
            damage_operator="+",
            effect=bonus_if(lambda ctx: any(is_special_energy(e) for e in ctx.attached_energies(ctx.attacker)), 100),
        ),
    ],
)