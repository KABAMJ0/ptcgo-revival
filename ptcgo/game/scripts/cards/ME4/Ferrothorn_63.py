from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.effects import is_special_energy
from ptcgo.game.card_effects.attacks_common import bonus_if

card = PokemonCardDef(
    guid="7442b6a5-8498-5001-96e4-60cff8ea13b3",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ferrothorn.Name",
    display_name="Ferrothorn",
    searchable_by=["Ferrothorn", "Stage 1", "Ferrothorn"],
    subtypes=["Stage 1"],
    collector_number=63,
    set_code="ME4",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ferroseed.Name",
    family_id=597,
    abilities=[
        Ability(
            title="Startling Drop",
            game_text="During your opponent's turn, if this Pok\u00e9mon is discarded from your deck by an effect of an attack or Ability from your opponent's Pok\u00e9mon, or by an effect of your opponent's Item or Supporter cards, discard the top 8 cards of your opponent's deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Special Whip",
            game_text="If this Pok\u00e9mon has any Special Energy attached, this attack does 70 more damage.",
            cost={PokemonTypes.METAL: 2},
            damage=70,
            damage_operator="+",
            effect=bonus_if(lambda ctx: any(is_special_energy(e) for e in ctx.attached_energies(ctx.attacker)), 70),
        ),
    ],
)