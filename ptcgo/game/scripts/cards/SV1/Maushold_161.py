from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5dcb5fcd-13c3-5869-ae1f-ff333d25611a",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Maushold.Name",
    display_name="Maushold",
    searchable_by=["Maushold", "Stage 1", "Maushold"],
    subtypes=["Stage 1"],
    collector_number=161,
    set_code="SV1",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tandemaus.Name",
    family_id=924,
    abilities=[
        Attack(
            title="Slap",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
        Attack(
            title="Family Attack",
            game_text="This attack does 70 damage for each of your Maushold in play.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=70,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)