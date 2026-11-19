from ptcgo.game.card_effects.attacks_common import spread_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import spread_damage

card = PokemonCardDef(
    guid="b8482cef-e79d-5e68-8549-21d5434f9637",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NsVanilluxe.Name",
    display_name="N's Vanilluxe",
    searchable_by=["N's Vanilluxe", "Stage 2", "NsVanilluxe"],
    subtypes=["Stage 2"],
    collector_number=51,
    set_code="ME2PT5",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.NsVanillish.Name",
    family_id=582,
    abilities=[
        Attack(
            title="Snow Coating",
            game_text="Double the number of damage counters on each of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=spread_damage(10, side="opponent", include_active=False),
        ),
        Attack(
            title="Blizzard",
            game_text="This attack also does 10 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=spread_damage(10, side="opponent", include_active=False),
        ),
    ],
)