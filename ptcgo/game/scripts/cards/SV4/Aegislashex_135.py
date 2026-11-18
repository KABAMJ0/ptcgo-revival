from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f9f4a954-43d9-5973-90a2-815fd7ea6766",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aegislashex.Name",
    display_name="Aegislash ex",
    searchable_by=["Aegislash ex", "Stage 2", "ex", "Aegislashex"],
    subtypes=["Stage 2", "ex"],
    collector_number=135,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=330,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Doublade.Name",
    family_id=679,
    abilities=[
        Attack(
            title="Peerless Edge",
            game_text="This attack does 70 damage for each Prize card you have taken.",
            cost={PokemonTypes.METAL: 1},
            damage=70,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Double-Edged Slash",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.METAL: 2},
            damage=220,
            effect=unimplemented,
        ),
    ],
)