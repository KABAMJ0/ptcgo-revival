from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8652ef01-b9cd-5e02-b402-7242e6d17557",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kakuna.Name",
    display_name="Kakuna",
    searchable_by=["Kakuna", "Stage 1", "Kakuna"],
    subtypes=["Stage 1"],
    collector_number=14,
    set_code="SV3PT5",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Weedle.Name",
    family_id=13,
    abilities=[
        Ability(
            title="Cocoon Cover",
            game_text="Prevent all effects of attacks used by your opponent's Pok\u00e9mon done to this Pok\u00e9mon. (Damage is not an effect.)",
            effect=unimplemented,
        ),
        Attack(
            title="Zzzt",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)