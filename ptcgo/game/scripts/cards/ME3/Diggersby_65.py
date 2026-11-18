from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="03fc01b0-c424-55bb-8713-52ad95a52c91",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Diggersby.Name",
    display_name="Diggersby",
    searchable_by=["Diggersby", "Stage 1", "Diggersby"],
    subtypes=["Stage 1"],
    collector_number=65,
    set_code="ME3",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bunnelby.Name",
    family_id=659,
    abilities=[
        Attack(
            title="Earthquake",
            game_text="This attack also does 30 damage to each of your Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            damage=140,
            effect=unimplemented,
        ),
        Attack(
            title="Whap Down",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
        ),
    ],
)