from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack, snipe_attack, spread_damage, place_counters, bonus_if
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID

card = PokemonCardDef(
    guid="209aa523-32fc-5c4d-9a3c-5099c5a30a3f",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LarrysStaraptor.Name",
    display_name="Larry's Staraptor",
    searchable_by=["Larry's Staraptor", "Stage 2", "LarrysStaraptor"],
    subtypes=["Stage 2"],
    collector_number=170,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.LarrysStaravia.Name",
    family_id=396,
    abilities=[
        Attack(
            title="Facade",
            game_text="If this Pok\u00e9mon is Burned or Poisoned, this attack does 100 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            effect=bonus_if(lambda ctx: any(c in (ctx.attacker.get_attribute(AttrID.SPECIAL_CONDITIONS) or []) for c in ("Burned", "Poisoned")), 100),
        ),
        Attack(
            title="Feathery Strike",
            game_text="Discard 2 Energy from this Pok\u00e9mon, and this attack also does 50 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 3},
            damage=150,
            effect=self_energy_discard_attack(count=2, before_damage=True, also=snipe_attack(50, pool="bench", count=1)),
        ),
    ],
)