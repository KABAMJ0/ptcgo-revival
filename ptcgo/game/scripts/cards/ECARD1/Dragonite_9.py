from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f9d08e6c-bf52-5515-9d41-925536228fd0",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonite.Name",
    display_name="Dragonite",
    searchable_by=["Dragonite", "Stage 2", "Dragonite"],
    subtypes=["Stage 2"],
    collector_number=9,
    set_code="ECARD1",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name",
    family_id=147,
    abilities=[
        Ability(
            title="Tailwind",
            game_text="Once during your turn (before your attack), if Dragonite is on your Bench, you may reduce your Active Pok\u00e9mon's Retreat Cost to 0.",
            effect=unimplemented,
        ),
        Attack(
            title="Dragon Tail",
            game_text="Flip 2 coins. This attack does 40 damage times the number of heads.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.WATER: 1, PokemonTypes.FIGHTING: 1},
            damage=40,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=40),
        ),
    ],
)