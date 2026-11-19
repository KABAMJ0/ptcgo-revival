from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_damage

card = PokemonCardDef(
    guid="24a6bc68-41ff-5f97-8911-8f65da2932b7",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kabutops.Name",
    display_name="Kabutops",
    searchable_by=["Kabutops", "Stage 2", "Kabutops"],
    subtypes=["Stage 2"],
    collector_number=150,
    set_code="ECARD3",
    rarity=Rarities.RareSecret,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kabuto.Name",
    family_id=140,
    abilities=[
        Ability(
            title="Crystal Type",
            game_text="Whenever you attach a Water, Lightning, or Fighting basic Energy card from your hand to Kabutops, Kabutops's type (color) becomes the same as that type of Energy until the end of the turn.",
            effect=unimplemented,
        ),
        Attack(
            title="Draining Cut",
            game_text="Remove a damage counter from Kabutops.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Triple Cutter",
            game_text="Flip 3 coins. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=flip_damage(coins=3, per_heads=30),
        ),
    ],
)