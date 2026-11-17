from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bffb3971-6bfc-5ff4-877e-819053800b7a",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ArcanineG.Name",
    display_name="Arcanine G",
    searchable_by=["Arcanine G", "Basic", "SP", "ArcanineG"],
    subtypes=["Basic", "SP"],
    collector_number=15,
    set_code="PL3",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=59,
    abilities=[
        Ability(
            title="Extreme Speed",
            game_text="Arcanine G's Retreat Cost is Colorless less for each Fire Energy attached to Arcanine G.",
            effect=unimplemented,
        ),
        Attack(
            title="Overrun",
            game_text="Does 20 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=unimplemented,
        ),
    ],
)