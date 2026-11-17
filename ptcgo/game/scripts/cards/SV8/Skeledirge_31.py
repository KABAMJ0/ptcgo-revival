from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="faedccb4-b724-5d43-98fa-92077f02e26c",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skeledirge.Name",
    display_name="Skeledirge",
    searchable_by=["Skeledirge", "Stage 2", "Skeledirge"],
    subtypes=["Stage 2"],
    collector_number=31,
    set_code="SV8",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Crocalor.Name",
    family_id=909,
    abilities=[
        Ability(
            title="Unaware",
            game_text="Prevent all effects of attacks used by your opponent's Pok\u00e9mon done to this Pok\u00e9mon. (Damage is not an effect.)",
            effect=unimplemented,
        ),
        Attack(
            title="Torcherto",
            game_text="This attack does 20 more damage for each Benched Pok\u00e9mon (both yours and your opponent's).",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)