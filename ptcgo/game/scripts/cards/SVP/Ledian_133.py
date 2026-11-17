from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="06f5759e-109c-5f87-9082-8211198ad7a5",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ledian.Name",
    display_name="Ledian",
    searchable_by=["Ledian", "Stage 1", "Ledian"],
    subtypes=["Stage 1"],
    collector_number=133,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ledyba.Name",
    family_id=166,
    abilities=[
        Ability(
            title="Glittering Star Pattern",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may switch in 1 of your opponent's Benched Pok\u00e9mon that has 90 HP or less remaining to the Active Spot.",
            effect=unimplemented,
        ),
        Attack(
            title="Swift",
            game_text="This attack's damage isn't affected by Weakness or Resistance, or by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=unimplemented,
        ),
    ],
)