from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="29c3d237-9a25-52c6-abe3-71ece09b7ff4",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pecharuntex.Name",
    display_name="Pecharunt ex",
    searchable_by=["Pecharunt ex", "Basic", "ex", "Pecharuntex"],
    subtypes=["Basic", "ex"],
    collector_number=163,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
    hp=190,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=1025,
    abilities=[
        Ability(
            title="Subjugating Chains",
            game_text="Once during your turn, you may switch 1 of your Benched Darkness Pok\u00e9mon, except any Pecharunt ex, with your Active Pok\u00e9mon. If you do, the new Active Pok\u00e9mon is now Poisoned. You can't use more than 1 Subjugating Chains Ability each turn.",
            effect=unimplemented,
        ),
        Attack(
            title="Irritated Outburst",
            game_text="This attack does 60 damage for each Prize card your opponent has taken.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=60,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)